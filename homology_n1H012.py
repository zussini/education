from manim import *

class HomologyIn3D(ThreeDScene):
    def construct(self):
        # Camera settings
        self.move_camera(phi=25 * DEGREES, theta=-90 * DEGREES, frame_center=(0, 0, 0))

        # Function to create a grid of tori
        def create_torus_grid(rows, cols):
            tori = VGroup(*[Torus().set_fill(opacity=0.3) for _ in range(rows * cols)])
            tori.arrange_in_grid(rows, cols, buff=0.5)
            return tori

        # Grid configurations
        grid_sizes = [(1, 2), (2, 2), (2, 4), (4, 4)]

        for rows, cols in grid_sizes:
            # Create grid of tori
            torus_grid = create_torus_grid(rows, cols)
            torus_grid.scale(0.75 / max(rows, cols))  # Scale down to fit the scene

            # Homology text
            torus_text = MathTex(rf"H_0 = {rows * cols}, \ ", r"H_1 = 1, \ ", r"H_2 = 1").to_edge(UP)
            torus_description = Text(f"{rows * cols} Tori", font_size=24).to_edge(DOWN)

            # Animate
            self.play(FadeIn(torus_grid), Write(torus_text), Write(torus_description))
            self.wait(2)
            self.play(FadeOut(torus_grid), FadeOut(torus_text), FadeOut(torus_description))

        self.clear()

if __name__ == "__main__":
    HomologyIn3D().render()

