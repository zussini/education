import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.decomposition import PCA
import matplotlib.colors as mcolors

N = 250  # Number of particles
delta_tau = 0.1  # Grid size
total_permutations = 250  # Total number of permutations
rows_to_plot = [0, 1, 2, 50, 249]  # Rows to plot (first 3 and last one)

# Sample data: 1D positions and momenta of particles
original_positions = np.random.rand(N)  # 1D positions
original_momenta = np.random.rand(N)    # 1D momenta
positions = original_positions.copy()
momenta = original_momenta.copy()

# Initialize PCA
pca = PCA(n_components=2)

# Create a figure for the selected rows
fig = plt.figure(figsize=(18, 6 * len(rows_to_plot)))

# Dictionary to keep track of permutation counts
permutation_counts = {i: 0 for i in range(N)}

# List to keep track of Gamma space data
gamma_space_data = [np.hstack((positions, momenta))]

# Function to plot a single row of diagrams
def plot_row(fig, plot_idx, positions, momenta, permutation_counts, gamma_space_data):
    # µ Space Scatter Plot
    ax1 = fig.add_subplot(len(rows_to_plot), 3, 3 * plot_idx + 1)
    # Plot all points in blue
    ax1.scatter(original_positions, original_momenta, color='blue')
    # Plot permuted points with gradient color
    for idx, count in permutation_counts.items():
        if count > 0:
            color = plt.cm.Reds(count / max(permutation_counts.values()))
            ax1.scatter(positions[idx], momenta[idx], color=color)
    ax1.set_xlabel('Position')
    ax1.set_ylabel('Momentum')
    ax1.set_title('µ Space Scatter Plot')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.grid(True)


    # µ Space Heatmap (using original positions and momenta)
    ax2 = fig.add_subplot(len(rows_to_plot), 3, 3 * plot_idx + 2)
    sns.histplot(
        x=original_positions, y=original_momenta, 
        bins=[np.arange(0, 1 + delta_tau, delta_tau), np.arange(0, 1 + delta_tau, delta_tau)], 
        cmap='viridis', cbar=True if plot_idx == 0 else False, ax=ax2
    )
    ax2.set_xlabel('Position')
    ax2.set_ylabel('Momentum')
    ax2.set_title('µ Space Heatmap')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)

    # Gamma Space Projection
    ax3 = fig.add_subplot(len(rows_to_plot), 3, 3 * plot_idx + 3)
    if len(gamma_space_data) > 1:
        pca.fit(np.array(gamma_space_data))
        points_2d = pca.transform(np.array(gamma_space_data))
        ax3.scatter(points_2d[:, 0], points_2d[:, 1], color='red')
    ax3.set_xlabel('PCA Component 1')
    ax3.set_ylabel('PCA Component 2')
    ax3.set_title('Gamma Space Projection')
    ax3.grid(True)


# Plot initial state
plot_row(fig, 0, positions, momenta, permutation_counts, gamma_space_data)

# Generate and plot permutations
plot_idx = 1
for i in range(1, total_permutations):
    # Select two random indices for permutation
    idx1, idx2 = np.random.choice(N, 2, replace=False)
    # Update permutation counts
    permutation_counts[idx1] += 1
    permutation_counts[idx2] += 1

    # Swap the positions and momenta of the selected indices
    positions[idx1], positions[idx2] = positions[idx2], positions[idx1]
    momenta[idx1], momenta[idx2] = momenta[idx2], momenta[idx1]

    # Update Gamma space data
    gamma_space_data.append(np.hstack((positions, momenta)))

    # Plot only the specified rows
    if i in rows_to_plot:
        plot_row(fig, plot_idx, positions, momenta, permutation_counts, gamma_space_data)
        plot_idx += 1

plt.tight_layout()
plt.show()

