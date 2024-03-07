
import matplotlib.pyplot as plt
import numpy as np

# Adjusting the script to include labels for both standard and reduced homologies

# Initialize the figure with 3 subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Example 1: Path-Connected Space (Sphere or Circle)
theta = np.linspace(0, 2*np.pi, 100)
x1 = np.cos(theta)
y1 = np.sin(theta)
axs[0].plot(x1, y1)
axs[0].set_title("$H_0 = \\mathbb{Z}$\nPath-Connected Space")
axs[0].text(0, -1.2, "$\\tilde{H}_0 = 0$", ha='center')
axs[0].axis('equal')
axs[0].axis('off')

# Example 2: Two Discrete Points
axs[1].plot([0, 1], [0, 0], 'o')
axs[1].set_title("$H_0 = \\mathbb{Z} \\times \\mathbb{Z}$\nTwo Discrete Points")
axs[1].text(0.5, -0.6, "$\\tilde{H}_0 = \\mathbb{Z}$", ha='center')
axs[1].axis('equal')
axs[1].axis([-0.5, 1.5, -0.5, 0.5])
axs[1].axis('off')

# Example 3: Three Separate Circles
for i in range(3):
    circle = plt.Circle((i, 0), 0.4, fill=False, edgecolor='black')
    axs[2].add_patch(circle)
axs[2].set_title("$H_0 = \\mathbb{Z}^3$\nThree Separate Circles")
axs[2].text(1, -1, "$\\tilde{H}_0 = \\mathbb{Z}^2$", ha='center')
axs[2].axis('equal')
axs[2].axis([-1, 3, -1, 1])
axs[2].axis('off')

# Show the plot
plt.tight_layout()
plt.show()

