from manim import *

class HomologyIn3D(ThreeDScene):
    def construct(self):
        # Camera settings
        self.move_camera(phi=25 * DEGREES, theta=-90 * DEGREES, frame_center=(0, 0, 0))

        # Function to create a grid of tori
        def create_torus_grid(rows, cols, major_radius, minor_radius):
            distance = 2 * (major_radius + minor_radius)
            tori = VGroup(*[Torus(major_radius=major_radius, minor_radius=minor_radius).set_fill(opacity=0.3) for _ in range(rows * cols)])
            for k in range(rows * cols):
                row = k // cols
                col = k % cols
                tori[k].move_to(np.array([distance * col, distance * row, 0]))
            return tori

        # Function to create a group of hollow spheres
        # Function to create a group of hollow spheres in a line
        def create_hollow_spheres(num, radius):
            spheres = VGroup(*[Sphere(radius=radius).set_fill(opacity=0.3) for _ in range(num)])
            spheres.arrange(RIGHT, buff=2*radius)  # Arrange spheres in a line
            return spheres

        # Sequentially create and display the tori grid
        grid_sizes = [(1, 2), (2, 2), (2, 4), (4, 4)]
        for rows, cols in grid_sizes:
            torus_grid = create_torus_grid(rows, cols, 1, 0.25)
            torus_grid.scale(0.5)
            self.play(FadeIn(torus_grid))
            self.wait(2)
            if (rows, cols) != (4, 4):
                self.play(FadeOut(torus_grid))

        # Homology text for 4x4 tori grid
        torus_text = MathTex(r"H_0 = 1, \ ", rf"H_1 = 16, \ ", rf"H_2 = 16").to_edge(UP)
        self.play(Write(torus_text))

        # Transform half of the 4x4 grid into hollow spheres
        num_spheres = 8
        hollow_spheres = create_hollow_spheres(num_spheres, 1)
        hollow_spheres.move_to(ORIGIN)
        hollow_spheres.scale(0.5)

        # Homology text after transformation
        transformed_text = MathTex(r"H_0 = 1, \ ", r"H_1 = 8, \ ", rf"H_2 = {num_spheres}").to_edge(UP)


        # Reduce the radius of tori and spheres to create separation
        reduced_radius_torus_grid = create_torus_grid(2, 2, 0.75, 0.25)
        reduced_radius_spheres = create_hollow_spheres(2, 0.75)
        reduced_radius_spheres.move_to(ORIGIN)
        reduced_radius_spheres.scale(0.5)

        # Combine tori and spheres
        combined_objects = VGroup(reduced_radius_torus_grid, reduced_radius_spheres)
        combined_objects.arrange_in_grid(2, 2, buff=1)
        combined_objects.scale(0.5)

        # Homology text for separated objects
        separated_text = MathTex(r"H_0 = 4, \ ", r"H_1 = 2, \ ", r"H_2 = 2").to_edge(UP)

        # Animate separation
        self.play(
            Transform(torus_grid, combined_objects),
            Transform(torus_text, separated_text)
        )
        self.wait(2)

        self.clear()

if __name__ == "__main__":
    HomologyIn3D().render()

