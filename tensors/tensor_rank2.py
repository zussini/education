import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

# Original grid
x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)
X, Y = np.meshgrid(x, y)

# Transformation matrix (example)
T = np.array([[2, 1], [1, 2]])

# Apply transformation
X_trans = T[0, 0] * X + T[0, 1] * Y
Y_trans = T[1, 0] * X + T[1, 1] * Y

# Plot original grid
ax.plot(X, Y, 'k--', alpha=0.3)
ax.plot(X.T, Y.T, 'k--', alpha=0.3)

# Plot transformed grid
ax.plot(X_trans, Y_trans, 'r')
ax.plot(X_trans.T, Y_trans.T, 'r')

ax.set_aspect('equal')
ax.set_title('Covariant Matrix (Rank 2 Tensor)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()

