import matplotlib.pyplot as plt
import numpy as np

def plot_non_overlapping_loop(ax, radius, center, winding_number, color):
    """
    Plot a non-overlapping loop around the circle with a given winding number.
    Adjusts the radius slightly for each loop to avoid overlap.
    """
    adjusted_radius = radius + 0.1 * winding_number
    theta = np.linspace(0, 2 * np.pi * winding_number, 300 * abs(winding_number))
    x = center[0] + adjusted_radius * np.cos(theta)
    y = center[1] + adjusted_radius * np.sin(theta)
    ax.plot(x, y, color=color, label=f"Winding number: {winding_number}")

# Create a new figure and axis
fig, ax = plt.subplots()
# Draw a circle
circle_radius = 1
circle_center = (0, 0)
# Draw a circle
circle = plt.Circle(circle_center, circle_radius, color='lightgray', fill=False)
ax.add_artist(circle)

# Draw non-overlapping loops with different winding numbers
plot_non_overlapping_loop(ax, circle_radius, circle_center, 1, 'blue')  # Winding number 1
plot_non_overlapping_loop(ax, circle_radius, circle_center, -2, 'red')  # Winding number -2
plot_non_overlapping_loop(ax, circle_radius, circle_center, 3, 'green')  # Winding number 3

# Set limits and labels
ax.set_xlim(-1.5, 2.5)
ax.set_ylim(-1.5, 2.5)
ax.set_aspect('equal', adjustable='box')
ax.legend()
ax.set_title('Non-Overlapping Loops with Different Winding Numbers Around \n  a Circle presenting fundamental group concept')

# Show the plot
plt.show()

~                                                                                                                                                                                                          
~                                                                                                                                                                                                          
~                                                                                                                                                                                                          
~                    
