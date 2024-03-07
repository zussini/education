from manim import *

class EulerCharacteristic(ThreeDScene):
    def construct(self):
        # Create a Sphere (polyhedron) - you can design this to look like a soccer ball
        sphere = Sphere()
        
        # Add labels or pointers to count vertices (V), edges (E), and faces (F)
        # For simplicity, these are just placeholders.
        V_count = Text("V = [count]", font_size=24).to_edge(UP)
        E_count = Text("E = [count]", font_size=24).to_edge(UP)
        F_count = Text("F = [count]", font_size=24).to_edge(UP)
        euler_formula = MathTex(r"\chi = V - E + F").to_edge(DOWN)
        euler_result = Text("For a sphere, χ = 2", font_size=24).to_edge(DOWN)

        # Animation to show the sphere
        self.play(Create(sphere))
        self.wait(1)

        # Show the counts and Euler characteristic
        self.play(Write(V_count), Write(E_count), Write(F_count))
        self.wait(2)

        self.play(Write(euler_formula))
        self.wait(2)

        # Show the result
        self.play(Write(euler_result))
        self.wait(2)

        self.clear()

if __name__ == "__main__":
    EulerCharacteristic().render()

