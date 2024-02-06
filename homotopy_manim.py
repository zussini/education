from manim import *

class HomotopyExample(Scene):
    def construct(self):
        # Create a circle
        circle = Circle(color=BLUE)

        # Define the start and end loops
        start_loop = self.get_loop(1, color=GREEN)
        end_loop = self.get_loop(0, color=RED)

        # Equation
        equation = MathTex(r"\mathbf{r}(t) = (\cos(2\pi t \cdot w), \sin(2\pi t \cdot w))",
                           substrings_to_isolate="w")
        equation.set_color_by_tex("w", YELLOW)
        equation.to_edge(UP)

        # Winding number
        winding_number = Tex("Winding number: w = 1").set_color(YELLOW).next_to(equation, DOWN)

        # Description text
        description_start = Text("Loop winding once around the circle").to_edge(DOWN)
        description_end = Text("Loop contracted to a point").to_edge(DOWN)

        # Add the circle, the start loop, the equation, and the starting description to the scene
        self.play(Create(circle), Create(start_loop), Write(equation), Write(winding_number), Write(description_start))
        self.wait(1)

        # Transform the start loop to the end loop, update the winding number, and change the description
        self.play(Transform(start_loop, end_loop), Transform(winding_number, Tex("Winding number: w = 0").set_color(YELLOW).next_to(equation, DOWN)), Transform(description_start, description_end))
        self.wait(1)

    def get_loop(self, winding_number, color):
        """
        Get a loop with a given winding number.
        """
        loop = ParametricFunction(
            lambda t: np.array([
                np.cos(2 * np.pi * t * winding_number),
                np.sin(2 * np.pi * t * winding_number),
                0
            ]),
            t_range=[0, 1],
            color=color
        )
        return loop

# To run and render the scene, use the following command in the terminal:
# manim -pql homotopy_manim.py HomotopyExample

~                                                    
