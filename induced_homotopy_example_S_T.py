from manim import *

class InducedHomomorphismExample(ThreeDScene):
    def construct(self):
        # Create a circle (S^1)
        circle = Circle(color=BLUE).shift(LEFT * 3)

        # Create a torus
        major_radius, minor_radius = 1, 0.3
        torus = Torus(major_radius=major_radius, minor_radius=minor_radius, color=GREEN).shift(RIGHT * 3)

        # Define a loop on the circle
        loop_on_circle = Circle(radius=0.2, color=RED).move_to(circle.get_center() + RIGHT * 0.5)

        # Place a corresponding loop on the torus
        loop_on_torus = Circle(radius=0.2, color=RED)
        loop_on_torus.move_to(torus.get_center() + RIGHT * major_radius + OUT * minor_radius)
        loop_on_torus.rotate(PI/2, axis=RIGHT)

        # Add the circle, torus, and loop on the circle
        self.add(circle, torus, loop_on_circle)
        self.move_camera(PI/3, PI/4)
        self.wait(1)

        # Animate the movement of the loop from the circle to the torus
        self.play(Transform(loop_on_circle, loop_on_torus))
        self.wait(1)

        # Function to update the loop's position and orientation on the torus
        def update_loop_on_torus(loop, alpha):
            theta = 2 * PI * alpha  # Full rotation
            new_loop = Circle(radius=0.2, color=RED)
            new_pos = torus.get_center() + np.array([major_radius * np.cos(theta), major_radius * np.sin(theta), minor_radius])
            new_loop.move_to(new_pos)
            new_loop.rotate(theta, axis=UP)
            new_loop.rotate(PI/2, axis=RIGHT)
            loop.become(new_loop)

        # Animate the loop rotating around the major radius of the torus
        self.play(UpdateFromAlphaFunc(loop_on_torus, update_loop_on_torus), run_time=4, rate_func=linear)
        self.wait(1)

# To run and render the scene, use the following command in the terminal:
# manim -pql your_script_name.py InducedHomomorphismExample

