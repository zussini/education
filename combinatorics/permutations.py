from manim import *

class PermutationScene(Scene):
    def construct(self):
        # Create 4 distinct balls
        balls = [Circle(color=color, fill_opacity=1).scale(0.5) for color in [RED, BLUE, GREEN, YELLOW]]
        ball_group = VGroup(*balls).arrange(RIGHT, buff=1)
        self.play(FadeIn(ball_group))
        self.wait(1)

        # Permutations without repetitions (4!)
        perm_text = Text("Permutations without Repetitions (4!)").to_edge(UP)
        self.play(Write(perm_text))
        self.wait(1)

        # Animate permutations without repetitions
        for i in range(4):
            self.play(ball_group[i].animate.move_to(UP * 2 + LEFT * 3 + RIGHT * i))
        self.wait(2)

        # Show the number of permutations (4!)
        permutations = MathTex("4! = 4 \\times 3 \\times 2 \\times 1 = 24").to_edge(DOWN)
        self.play(Write(permutations))
        self.wait(2)
        self.play(FadeOut(ball_group), FadeOut(permutations))

        # Permutations with repetitions (4^4)
        ball_group = VGroup(*balls).arrange(RIGHT, buff=1)
        self.play(FadeIn(ball_group))
        self.wait(1)

        perm_text_2 = Text("Permutations with Repetitions (4^4)").to_edge(UP)
        self.play(Transform(perm_text, perm_text_2))
        self.wait(1)

        # Animate permutations with repetitions
        # [This part can be represented by showing each ball in each position in a loop]
        # This is a simplified representation and may be adjusted for clarity.
        for i in range(4):
            self.play(ball_group[i].animate.move_to(UP * 2 + LEFT * 3 + RIGHT * i))
        self.wait(2)

        # Show the number of permutations (4^4)
        permutations_2 = MathTex("4^4 = 4 \\times 4 \\times 4 \\times 4 = 256").to_edge(DOWN)
        self.play(Transform(permutations, permutations_2))
        self.wait(2)

        # Conclusion
        self.play(FadeOut(ball_group), FadeOut(permutations), FadeOut(perm_text))

# To run this scene, use the following command:
# manim -pql script_name.py PermutationScene

