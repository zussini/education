import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# Define the line segment (space X)
x = np.linspace(0, 10, 400)
ax.plot(x, np.zeros_like(x), 'k-', label='Space X (Line Segment)')

# Define functions on different open subsets
x1 = np.linspace(2, 6, 400)
y1 = np.sin(x1)
ax.plot(x1, y1, 'b-', label='Function on Subset U1')

x2 = np.linspace(4, 8, 400)
y2 = 0.5 * x2 - 2
ax.plot(x2, y2, 'r-', label='Function on Subset U2')

# Highlighting the intersection
x_int = np.linspace(4, 6, 400)
y_int1 = np.sin(x_int)
y_int2 = 0.5 * x_int - 2
ax.fill_between(x_int, y_int1, y_int2, color='purple', alpha=0.3, label='Intersection U1 ∩ U2')

# Annotations and labels
ax.set_ylim(-2, 2)
ax.legend()
ax.set_title("Visualization of a Sheaf of Functions")
ax.set_xlabel("Space X")
ax.set_ylabel("Function Values")
ax.axhline(0, color='black',linewidth=0.5)
ax.set_yticks([])
ax.set_xticks([])

plt.show()
