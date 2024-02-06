import numpy as np
import matplotlib.pyplot as plt

# Define a function for the first loop (circle)
def loop1(t):
    return np.array([np.cos(2 * np.pi * t), np.sin(2 * np.pi * t)])

# Define a function for the second loop (ellipse)
def loop2(t):
    a = 2  # Major axis length
    b = 1  # Minor axis length
    return np.array([a * np.cos(2 * np.pi * t), b * np.sin(2 * np.pi * t)])

t_values = np.linspace(0, 1, 100)

fig, ax = plt.subplots()

ax.plot(*loop1(t_values), label='Loop 1 (circle)', color='blue')

ax.plot(*loop2(t_values), label='Loop 2 (ellipse)', color='red')

# Add a legend
ax.legend()

# Set axis limits
ax.set_xlim(-3, 3)
ax.set_ylim(-2, 2)

# Title and labels
ax.set_title('Example of homotopy between Two Loops')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Show the plot
plt.show()

~                              
