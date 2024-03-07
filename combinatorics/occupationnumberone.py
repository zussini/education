import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA

N = 200  # Number of particles
delta_tau = 0.1  # Grid size

# Sample data: positions and momenta of particles
positions = np.random.rand(N, 3)  # 3D positions
momenta = np.random.rand(N, 3)    # Corresponding momenta

# Create a figure and a set of subplots
fig, axs = plt.subplots(1, 3, figsize=(24, 6))

# µ Space Scatter Plot
axs[0].scatter(positions[:, 0], momenta[:, 0])
axs[0].set_xlabel('Position (x)')
axs[0].set_ylabel('Momentum ($p_x$)')
axs[0].set_title('µ Space Scatter Plot with Uniform Grid')
axs[0].grid(True)
axs[0].set_xticks(np.arange(0, 1.1, delta_tau))
axs[0].set_yticks(np.arange(0, 1.1, delta_tau))
axs[0].set_xlim(0, 1)
axs[0].set_ylim(0, 1)

# µ Space Heatmap
sns.histplot(
    x=positions[:, 0], y=momenta[:, 0], 
    bins=[np.arange(0, 1 + delta_tau, delta_tau), np.arange(0, 1 + delta_tau, delta_tau)], 
    cmap='viridis', cbar=True, ax=axs[1]
)
axs[1].set_xlabel('Position (x)')
axs[1].set_ylabel('Momentum ($p_x$)')
axs[1].set_title('µ Space Heatmap with Uniform Bins')
axs[1].set_xlim(0, 1)
axs[1].set_ylim(0, 1)

# Gamma Space Projection
positions1 = positions  # Use the same positions for the first point
momenta1 = momenta      # Use the same momenta for the first point
positions2 = np.random.rand(N, 3)  # New positions for the second point
momenta2 = np.random.rand(N, 3)    # New momenta for the second point

# Create two 6N-dimensional points
gamma_space_point1 = np.hstack((positions1.flatten(), momenta1.flatten()))
gamma_space_point2 = np.hstack((positions2.flatten(), momenta2.flatten()))

# Combine points to form a dataset for PCA
gamma_space_data = np.vstack((gamma_space_point1, gamma_space_point2))

# Apply PCA to project these points onto 2D
pca = PCA(n_components=2)
points_2d = pca.fit_transform(gamma_space_data)

# Plotting the projected point in 2D
axs[2].scatter(points_2d[0, 0], points_2d[0, 1], color='red')
axs[2].set_xlabel('PCA Component 1')
axs[2].set_ylabel('PCA Component 2')
axs[2].set_title('Projected Points in 2D from Gamma Space')
axs[2].grid(True)

# Display the plots
plt.tight_layout()
plt.show()

