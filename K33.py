from manim import *
from itertools import product

class K33GraphScene(ThreeDScene):
    def construct(self):
        # Define initial positions for the vertices of K3,3 in 2D
        pos_2d = {
            0: np.array([-1, 1, 0]),
            1: np.array([0, 1, 0]),
            2: np.array([1, 1, 0]),
            3: np.array([-1, -1, 0]),
            4: np.array([0, -1, 0]),
            5: np.array([1, -1, 0])
        }

        # Define final positions for the vertices of K3,3 in 3D
        pos_3d = {
            **pos_2d,
            0: np.array([-2, 1, 1]),
            2: np.array([1, 1, -1]),
            3: np.array([-1, -2, 2]),
            5: np.array([1, -1, 1])
        }

        # Create spheres for each vertex
        spheres = [Sphere(radius=0.1).move_to(pos) for pos in pos_2d.values()]

        # Create lines (edges) for the initial 2D configuration
        edges_2d = [Line(pos_2d[u], pos_2d[v]) for u, v in product(range(3), range(3, 6))]

        # Create lines (edges) for the final 3D configuration
        edges_3d = [Line(pos_3d[u], pos_3d[v]) for u, v in product(range(3), range(3, 6))]
        # Create line objects (edges) for the initial 2D configuration
        edges_2d = [Line(pos_2d[u], pos_2d[v]) for u, v in product(range(3), range(3, 6))]
        # Add these lines to the scene
        for edge in edges_2d:
            self.add(edge)

        # Animate the transformation of the graph to 3D
        for i, (u, v) in enumerate(product(range(3), range(3, 6))):
            # Create a new line for the 3D position
            new_line = Line(pos_3d[u], pos_3d[v])
            # Transform the old line to the new line
            self.play(Transform(edges_2d[i], new_line))

        # Add spheres to the scene
        for sphere in spheres:
            self.add(sphere)

        # Animate the movement of the spheres to their 3D positions
        for i in range(6):
            self.play(spheres[i].animate.move_to(pos_3d[i]))

        # Animate moving vertices and transforming edges into 3D
        self.play(
            *[spheres[i].animate.move_to(pos_3d[i]) for i in [0, 2, 3, 5]],
            *[Transform(edges_2d[i], edges_3d[i]) 
              for i in range(len(edges_2d))]
        )
        
        self.move_camera(phi=40 * DEGREES, theta=-35 * DEGREES, frame_center=(0, 0, 0))
        self.wait(2)
        self.move_camera(phi=50 * DEGREES, theta=-65 * DEGREES, frame_center=(0, 0, 0))
        self.wait(2)
        self.move_camera(phi=60 * DEGREES, theta=-95 * DEGREES, frame_center=(0, 0, 0))
        self.wait(2)
        self.move_camera(phi=70 * DEGREES, theta=-135 * DEGREES, frame_center=(0, 0, 0))
        self.wait(2)
        self.move_camera(phi=80 * DEGREES, theta=-165 * DEGREES, frame_center=(0, 0, 0))
        self.wait(2)
        self.move_camera(phi=90 * DEGREES, theta=-195 * DEGREES, frame_center=(0, 0, 0))
        self.wait(2)
