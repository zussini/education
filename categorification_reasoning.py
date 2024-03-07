from manim import *

class NumberCategory(Scene):
    def construct(self):
        # Creating dots for natural numbers
        numbers = VGroup(*[Dot().shift(i*RIGHT) for i in range(5)])
        labels = VGroup(*[Text(str(i)).next_to(numbers[i], DOWN) for i in range(5)])

        # Creating arrows for addition morphisms
        arrows = VGroup(
            *[Arrow(numbers[i], numbers[i+1], buff=0.1) for i in range(4)]
        )

        self.play(Create(numbers), Write(labels))
        self.play(Create(arrows))
        self.wait(2)

