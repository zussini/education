from manim import *
from itertools import combinations

class K5GraphScene(ThreeDScene):
    def construct(self):
        # Define initial positions for the vertices of K5 in 2D (pentagon shape)
        pos_pentagon = {
            0: np.array([np.cos(0 * 2 * np.pi / 5), np.sin(0 * 2 * np.pi / 5), 0]),
            1: np.array([np.cos(1 * 2 * np.pi / 5), np.sin(1 * 2 * np.pi / 5), 0]),
            2: np.array([np.cos(2 * 2 * np.pi / 5), np.sin(2 * 2 * np.pi / 5), 0]),
            3: np.array([np.cos(3 * 2 * np.pi / 5), np.sin(3 * 2 * np.pi / 5), 0]),
            4: np.array([np.cos(4 * 2 * np.pi / 5), np.sin(4 * 2 * np.pi / 5), 0])
        }

        # Define final positions for the vertices of K5 in 3D (lifting two vertices)
        pos_3d = {
            **pos_pentagon,
            3: np.array([np.cos(3 * 2 * np.pi / 5), np.sin(3 * 2 * np.pi / 5), -1]), # Lower vertex 3
            4: np.array([np.cos(4 * 2 * np.pi / 5), np.sin(4 * 2 * np.pi / 5), 1])  # Lift vertex 4
        }

        # Create spheres for each vertex
        spheres = [Sphere(radius=0.1).move_to(pos) for pos in pos_pentagon.values()]

        # Create lines (edges) between each pair of spheres (vertices)
        edges = []
        for i in range(5):
            for j in range(i+1, 5):
                start, end = pos_pentagon[i], pos_pentagon[j]
                edge = Line(start, end)
                edges.append(edge)

        # Add spheres and edges to the scene
        for sphere in spheres:
            self.add(sphere)
        for edge in edges:
            self.add(edge)

        # Animate lifting two vertices to transform the graph into 3D
        self.play(
            spheres[3].animate.move_to(pos_3d[3]),
            spheres[4].animate.move_to(pos_3d[4]),
            *[Transform(edges[i], Line(pos_3d[j], pos_3d[k]))
              for i, (j, k) in enumerate(combinations(range(5), 2))]
        )

        # Rotate the camera for a better final view
        self.move_camera(phi=40 * DEGREES, theta=-35 * DEGREES, frame_center=(0, 0, 0))
        self.wait(1)
        self.move_camera(phi=60 * DEGREES, theta=-65 * DEGREES, frame_center=(0, 0, 0))
        self.wait(1)
        self.move_camera(phi=50 * DEGREES, theta=-95 * DEGREES, frame_center=(0, 0, 0))
        self.wait(1)
        self.move_camera(phi=40 * DEGREES, theta=-135 * DEGREES, frame_center=(0, 0, 0))
        self.wait(1)
        self.move_camera(phi=50 * DEGREES, theta=-165 * DEGREES, frame_center=(0, 0, 0))
        self.wait(1)
        self.move_camera(phi=60 * DEGREES, theta=-195 * DEGREES, frame_center=(0, 0, 0))
        self.wait(1)
