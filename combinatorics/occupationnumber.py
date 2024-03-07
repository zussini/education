import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
N=200
# Sample data: positions and momenta of particles
positions = np.random.rand(N, 3)  # 100 particles, 3D positions
momenta = np.random.rand(N, 3)    # Corresponding momenta

# Creating the scatter plot with uniform grid
plt.figure(figsize=(8, 6))
plt.scatter(positions[:, 0], momenta[:, 0])  # Plotting x position vs x momentum
plt.xlabel('Position (x)')
plt.ylabel('Momentum ($p_x$)')
plt.title('µ Space Scatter Plot with Uniform Grid')

# Define the size of your grid (delta tau)
delta_tau = 0.1
plt.grid(True)
plt.xticks(np.arange(0, 1.1, delta_tau))
plt.yticks(np.arange(0, 1.1, delta_tau))
plt.xlim(0, 1)
plt.ylim(0, 1)

plt.show()


import seaborn as sns

# Define the size of your grid (delta tau)
delta_tau = 0.1

# Creating a 2D histogram (heatmap) with uniform bins and a color bar
plt.figure(figsize=(8, 6))
ax = sns.histplot(
    x=positions[:, 0], y=momenta[:, 0], 
    bins=[np.arange(0, 1 + delta_tau, delta_tau), np.arange(0, 1 + delta_tau, delta_tau)], 
    cmap='viridis', cbar=True
)
plt.xlabel('Position (x)')
plt.ylabel('Momentum (p_x)')
plt.title('µ Space Heatmap with Uniform Bins')
plt.xlim(0, 1)
plt.ylim(0, 1)

plt.show()



positions1 = positions  # 3D positions for the first point
momenta1 = momenta    # Corresponding momenta for the first point

positions2 = np.random.rand(N, 3)  # 3D positions for the second point
momenta2 = np.random.rand(N, 3)    # Corresponding momenta for the second point

# Create two 6N-dimensional points
gamma_space_point1 = np.hstack((positions1.flatten(), momenta1.flatten()))
gamma_space_point2 = np.hstack((positions2.flatten(), momenta2.flatten()))

# Combine points to form a dataset for PCA
gamma_space_data = np.vstack((gamma_space_point1, gamma_space_point2))

# Apply PCA to project these points onto 2D
pca = PCA(n_components=2)
points_2d = pca.fit_transform(gamma_space_data)

# Plotting the projected points in 2D
plt.figure(figsize=(6, 6))
plt.scatter(points_2d[0, 0], points_2d[0, 1], color='red')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.title('Projected Points in 2D from Gamma Space')
plt.grid(True)

plt.show()

