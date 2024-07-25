import matplotlib.pyplot as plt
import numpy as np

# Define the original basis vectors
basis_vectors = np.array([[1, 0], [0, 1]])

# Define the transformation matrix (example: stretching and rotation)
T = np.array([[2, 0.5], [0.5, 2]])

# Define a contravariant vector in the original basis
contravariant_vector = np.array([2, 1])

# Apply the transformation to the basis vectors and the contravariant vector
transformed_basis_vectors = T @ basis_vectors
transformed_contravariant_vector = np.linalg.inv(T) @ contravariant_vector

fig, ax = plt.subplots()
origin = np.array([[0, 0], [0, 0]])  # origin points for basis vectors

# Plot original basis vectors
ax.quiver(*origin, basis_vectors[:, 0], basis_vectors[:, 1], color=['r', 'g'], scale=1, scale_units='xy', angles='xy')
ax.text(1.1, 0.1, 'e1', color='r')
ax.text(0.1, 1.1, 'e2', color='g')

# Plot transformed basis vectors
ax.quiver(*origin, transformed_basis_vectors[:, 0], transformed_basis_vectors[:, 1], color=['r', 'g'], alpha=0.5, scale=1, scale_units='xy', angles='xy')
ax.text(2.1, 0.6, 'T(e1)', color='r', alpha=0.5)
ax.text(0.6, 2.1, 'T(e2)', color='g', alpha=0.5)

# Plot the original contravariant vector
ax.quiver(0, 0, contravariant_vector[0], contravariant_vector[1], color='b', scale=1, scale_units='xy', angles='xy')
ax.text(2.1, 1.1, 'v', color='b')

# Plot the transformed contravariant vector
ax.quiver(0, 0, transformed_contravariant_vector[0], transformed_contravariant_vector[1], color='b', alpha=0.5, scale=1, scale_units='xy', angles='xy')
ax.text(0.8, 0.5, 'T^{-1}(v)', color='b', alpha=0.5)

# Annotate the type of transformation
ax.text(0, 4.8, 'Contravariant Transformation:', fontsize=12, color='black')
ax.text(0, 4.5, r'$T^{-1}$', fontsize=12, color='black')

# Display transformation matrix
transformation_matrix_str = r'$T = \begin{bmatrix} 2 & 0.5 \\ 0.5 & 2 \end{bmatrix}$'
ax.text(-0.5, 5.5, transformation_matrix_str, fontsize=12, color='black', transform=ax.transAxes)

ax.set_aspect('equal')
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.grid()
plt.title('Contravariant Vector Transformation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

