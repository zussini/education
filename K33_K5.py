from manim import *

class CompleteBipartiteGraphScene(ThreeDScene):
    def construct(self):
        # Hard-code the values for n and k
        n = 3
        k = 3

        # Define the positions for the vertices in 3D space
        pos_n = {i: np.array([2 * i, 0, 0]) for i in range(n)}
        pos_k = {j + n: np.array([2 * j, 2, 0]) for j in range(k)}

        # Combine the positions
        pos = {**pos_n, **pos_k}

        # Define the edges
        edges = [(i, j + n) for i in range(n) for j in range(k)]

        # Create the graph
        G = Graph(list(pos.keys()), edges, layout=pos, labels=True)

        # Add the graph to the scene
        self.add(G)

        # (Optional) Animate the graph, e.g., rotate
        #self.play(Rotate(G, angle=PI, axis=UP))

        # (Optional) Add more animations or customize as needed

# To render this scene, use the following command in the command line:
# manim -pql your_script.py CompleteBipartiteGraphScene

